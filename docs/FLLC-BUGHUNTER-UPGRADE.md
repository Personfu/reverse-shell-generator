# FLLC Bug Hunter Upgrade — reverse-shell-generator

## Portfolio role

This repository is a high-risk dual-use reference. It can still fit the FLLC portfolio, but only as an **authorized lab, CTF, payload literacy, and detection engineering reference**.

The public story should not be “generate shells against targets.” It should be:

> Understand payload syntax, listener mechanics, and defensive detection patterns in owned labs, CTFs, and authorized red-team exercises.

## FLLC upgrade path

### 1. Add lab mode first

Create a default `Lab Mode` page that:

- states the scope boundary;
- defaults to localhost examples;
- explains listener/payload concepts at a high level;
- links to detection notes;
- warns against unauthorized use.

### 2. Detection engineering companion

Add a detection companion page:

- common process ancestry patterns;
- suspicious outbound connection concepts;
- shell spawning telemetry;
- logging requirements;
- lab-only Sigma/YARA-style ideas without operational abuse instructions.

### 3. CTF / owned-lab templates

Add templates for legal training contexts:

```text
Lab name:
Host owned by:
Network isolated: yes/no
Payload used:
Listener used:
Telemetry captured:
Detection written:
Lessons learned:
Cleanup performed:
```

### 4. Website integration

Feature as a **paid/member detection lab**, not public tooling:

- `Payload Literacy Lab`.
- `Reverse Shell Detection Primer`.
- `CTF Listener Mechanics`.
- `Telemetry-to-Detection Workflow`.

## Content outputs

- Blog: “Reverse shells as detection lessons, not internet toys.”
- Short video: “If you cannot explain the telemetry, do not run the payload.”
- Member lesson: “Build a reverse-shell lab and write the detection.”

## Professional rules

- CTFs, owned labs, or written authorization only.
- No third-party targets.
- No persistence or stealth content.
- No bypass claims.
- Cleanup and evidence handling required.
