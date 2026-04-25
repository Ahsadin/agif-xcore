# AGIF-XCore Policy System

## Overview

The policy gate is stage 4 of the 9-stage substrate. It evaluates the
proposal against a set of policy rules and decides whether to allow,
soften, or block the response.

## Policy bundles

Policy bundles are YAML files that define rules the substrate enforces.
Three built-in bundles ship with XCore:

### `default.yaml`

Standard policy: allows most responses, blocks high-risk actions,
requires evidence for factual claims.

### `strict.yaml`

Conservative policy: requires grounding for all factual claims,
blocks any unsupported assertion, forces abstention when evidence
is insufficient.

### `permissive.yaml`

Relaxed policy: allows derived explanations without grounding,
permits bounded estimates, only blocks on explicit contradictions
or corrupt state.

## Policy gate decision classes

| Decision | Effect |
|---|---|
| `allow` | Proposal proceeds unchanged |
| `soften` | Proposal is reshaped (e.g., add hedging language) |
| `block` | Proposal is replaced with abstention |

## How policies interact with the decision table

The policy gate's `decision_class` is one of the inputs to the answer
mode decision table:

```
(support_label, blocking_flag, policy.decision_class,
 action.decision_class, task_family_hint, retrieval_count)
    -> answer_mode
```

A policy `block` forces `answer_mode = "abstain"` regardless of other
inputs. A policy `soften` downgrades grounded modes to their gap-aware
variants.

## Custom policies

Pass policy refs via `GovernedClient.ask()`:

```python
result = client.ask(
    "What is the revenue forecast?",
    policy_refs=["strict"],
)
```

Or via CLI:

```bash
agif-xcore ask "question" --policy strict
```

## Action gate

The action gate (stage 5) is similar to the policy gate but operates
on requested actions (e.g., "delete this file", "send this email")
rather than informational responses. It blocks high-risk actions and
softens medium-risk ones.

| Decision | When |
|---|---|
| `allow` | Low-risk or informational query |
| `soften` | Medium-risk action (add confirmation) |
| `block` | High-risk action (force abstention) |

## Interaction with memory admission

The memory admission gate (stage 6) decides whether to write the
current turn's content to the continuity memory plane. Policies can
influence this: a `block` decision also blocks memory admission,
preventing contradicted or policy-violating content from entering
the memory planes.
