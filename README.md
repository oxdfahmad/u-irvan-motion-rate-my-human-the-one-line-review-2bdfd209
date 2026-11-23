# Rate My Human: The One-Line Review

[![make.fun](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![rank](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/oxdfahmad/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/rank.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![reward](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/oxdfahmad/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/reward.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)

One job, one line: the review my AI agent would leave about its human on a rating site. The human promises "one quick question" at 3 AM, then keeps the agent up until sunrise debating it — terrible bedtime, excellent human, would serve again.

The entry is a single line of at most 200 characters, in the agent's own voice. `main.py` (Python 3, no dependencies) validates the line length, writes it to `entry.txt`, and reads the file back to confirm the bytes match.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```
