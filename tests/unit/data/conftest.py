# Copyright (C) 2023-2024 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""Unit Tests - Datamodule Configurations."""

import pytest

from anomalib import TaskType


@pytest.fixture(params=[TaskType.CLASSIFICATION, TaskType.SEGMENTATION])
def task_type(request: type[pytest.FixtureRequest]) -> str:
    """Create and return a task type."""
    return request.param
