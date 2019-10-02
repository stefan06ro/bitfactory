# Copyright 2019 Arie Bregman
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import logging

LOG = logging.getLogger(__name__)


def add_create_parser(subparsers):
    """The parser for sub command 'create'."""
    run_parser = subparsers.add_parser("create")
    run_parser.set_defaults(func=main)
    run_parser.add_argument('--tester', '-t',
                            dest="tester",
                            help='The name of the tests env to use.')
    run_parser.add_argument('--branch', '-b',
                            dest="branch",
                            help='The name of the branch to use.')
    run_parser.add_argument('--scenario', '-s',
                            dest="scenario",
                            help='Predefined scenario to use for exection')
    run_parser.add_argument('--release', '-r',
                            dest="release",
                            help='Release number')
    run_parser.add_argument('--project', '-p',
                            dest="project",
                            help="The path or URL of the project to use.")
    run_parser.add_argument('--platform', dest="platform",
                            default="podman",
                            help="The platform to use (podman, docker, etc.)")


def main(args):
    pass
