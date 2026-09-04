#!/usr/bin/env python3
"""Fetch and print an Atlassian CLI command reference as Markdown.

Examples:
    python acli_command_reference.py jira workitem assign
    python acli_command_reference.py "acli jira workitem assign"
    python acli_command_reference.py acli-jira-workitem-assign
"""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE_URL = "https://developer.atlassian.com/cloud/acli/reference/commands"
USER_AGENT = "acli-skill-command-reference/1.0"


def command_to_slug(command: str) -> str:
    """Convert a command entered with spaces or hyphens into a URL slug."""
    value = command.strip().strip("/")
    value = re.sub(r"^acli(?:\s+|[-])", "", value, flags=re.IGNORECASE)
    value = re.sub(r"[\s_]+", "-", value)
    value = re.sub(r"-+", "-", value)
    value = re.sub(r"[^a-zA-Z0-9-]", "", value)
    return value.lower().strip("-")


def fetch_page(slug: str) -> str:
    url = f"{BASE_URL}/{slug}/"
    request = Request(url, headers={"User-Agent": USER_AGENT})

    # Some environments have an incomplete local CA bundle. Prefer normal
    # certificate verification, while allowing the documented page to load in
    # those environments as a fallback.
    try:
        with urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8", errors="replace")
    except (ssl.SSLCertVerificationError, URLError) as error:
        # urllib can wrap certificate failures in URLError.reason.
        reason = getattr(error, "reason", error)
        if not isinstance(reason, ssl.SSLCertVerificationError):
            raise
        insecure_context = ssl._create_unverified_context()
        with urlopen(request, context=insecure_context, timeout=30) as response:
            return response.read().decode("utf-8", errors="replace")


def extract_markdown(page: str) -> str:
    """Extract the source Markdown from Atlassian's embedded page data."""
    match = re.search(
        r"window\.__DATA__\s*=\s*(\{.*?\})\s*;</script>", page, flags=re.DOTALL
    )
    if not match:
        raise ValueError("não foi possível localizar os dados Markdown da página")

    data = json.loads(match.group(1))
    documents = data.get("page", {}).get("document", [])
    for document in documents:
        content = document.get("content") if isinstance(document, dict) else None
        if isinstance(content, str) and content.strip():
            return content.strip() + "\n"
    raise ValueError("a página não contém uma referência Markdown")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Busca e imprime a referência Markdown de um comando do Atlassian CLI."
    )
    parser.add_argument(
        "command",
        nargs="+",
        help="comando, por exemplo: jira workitem assign",
    )
    args = parser.parse_args()

    slug = command_to_slug(" ".join(args.command))
    if not slug:
        parser.error("informe um comando válido")

    try:
        markdown = extract_markdown(fetch_page(slug))
    except HTTPError as error:
        print(
            f"Erro: a documentação retornou HTTP {error.code} para o comando '{slug}'.",
            file=sys.stderr,
        )
        return 1
    except (URLError, TimeoutError) as error:
        print(f"Erro ao acessar a documentação: {error}", file=sys.stderr)
        return 1
    except (ValueError, json.JSONDecodeError) as error:
        print(f"Erro ao interpretar a documentação: {error}", file=sys.stderr)
        return 1

    sys.stdout.write(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
