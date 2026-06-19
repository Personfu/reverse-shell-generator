#!/usr/bin/env python3
"""Generate a defensive reverse-shell detection lab report template.

This file deliberately contains no payloads. It helps students document telemetry,
controls, and detections in an owned lab.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Reverse-Shell Detection Lab Report

Generated: {generated}
Lab owner: {owner}

## Authorized Scope

- Environment: owned lab / CTF / classroom only
- External targets: prohibited
- Payload storage: not included in this template

## Telemetry Checklist

- Process creation logs captured
- Parent/child process lineage reviewed
- Network egress destination recorded
- DNS queries reviewed
- EDR or Sysmon event IDs linked

## Detection Logic

Describe the observable behavior without publishing operational payloads.

## Timeline

| Time | Event | Evidence |
|---|---|---|
| TBD | Suspicious process started | TBD |
| TBD | Outbound connection observed | TBD |

## Remediation

- Restrict outbound egress
- Alert on unusual shell parent processes
- Add application control for high-risk interpreters
- Rotate any exposed lab credentials
"""


def main() -> None:
    parser = argparse.ArgumentParser(description='Create a defensive lab report template.')
    parser.add_argument('output', type=Path)
    parser.add_argument('--owner', default='FLLC lab')
    args = parser.parse_args()
    args.output.write_text(TEMPLATE.format(generated=datetime.now(timezone.utc).isoformat(), owner=args.owner), encoding='utf-8')
    print(f'wrote {args.output}')


if __name__ == '__main__':
    main()
