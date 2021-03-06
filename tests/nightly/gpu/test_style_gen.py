#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""
Test agents used with style-controlled generation.
"""

import unittest

import parlai.utils.testing as testing_utils
from parlai.core.opt import Opt


class TestClassifierOnGenerator(unittest.TestCase):
    """
    Test classifier on generator.
    """

    @testing_utils.retry()
    def test_simple(self):
        valid, test = testing_utils.train_model(
            Opt(
                dict(
                    task='integration_tests:classifier',
                    model='projects.style_gen.classifier:ClassifierAgent',
                    classes=['one', 'zero'],
                    optimizer='adamax',
                    truncate=8,
                    learningrate=7e-3,
                    batchsize=32,
                    num_epochs=5,
                    n_layers=1,
                    n_heads=1,
                    ffn_size=32,
                    embedding_size=32,
                )
            )
        )
        self.assertEqual(valid['accuracy'], 1.0)
        self.assertEqual(test['accuracy'], 1.0)


if __name__ == '__main__':
    unittest.main()
