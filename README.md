# MomoBird Team Memory plugins

The Claude and ChatGPT plugin packages are released under MIT. MomoBird names and trademarks remain with their respective owners.

Both packages use the same remote MCP endpoint and OAuth grant. A project manager chooses one operator-enabled MomoBird Pro project. The tools search approved memories and submit proposals. A proposal enters the review queue before it becomes searchable.

## Claude and Claude Code

The Claude package is under `claude/`. From the plugin repository root, validate it with `claude plugin validate ./claude --profile directory`. The directory submission uses the package's repository location.

For a manual Claude Code install from this repository, run:

```text
/plugin install momobird-team-memory --marketplace underestimatedme/momobird-team-memory-plugins
```

Claude can use the skill in an active conversation. This directory package uses the remote MCP connector and skill. The optional Claude Code capture hook is available in the manual package on the [main branch](https://github.com/underestimatedme/momobird-team-memory-plugins/tree/main).

## ChatGPT and Codex

Create the upload ZIP with `cd chatgpt && zip -r /tmp/momobird-team-memory.zip LICENSE plugin.json mcp.json skills assets`. The directory submission uses the portable package and its remote MCP server. It has no lifecycle hooks. Users can request capture as part of their active conversation. The host applies its tool confirmation policy.

## Review verification

Use a dedicated writable sample account with an operator-enabled Pro project and a second project without the memory purpose. Verify authentication, source attribution, search, duplicate retries, denial for the other project, pending visibility, approval, and revocation. The OpenAI submission requires a verified publisher, domain proof, a walkthrough, five positive and three negative review cases, and reviewer access entered in the portal. Submit Claude through its directory portal and check its review status separately.

This source release precedes directory approval. The connector requires the production team-memory endpoint and an operator-enabled Pro project.
