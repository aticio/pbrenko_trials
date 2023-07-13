#!/usr/bin/env python

from pbrenko_trials.repository.memrepo import MemRepo
from pbrenko_trials.use_cases.analyze import AnalyzeUseCase


repo = MemRepo()
analyze_use_case = AnalyzeUseCase()
result = analyze_use_case.analyze(repo, "BTCUSDT", "202101010000", "202301010000")

print(result)
