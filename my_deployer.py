#!/usr/bin/env python3
__author__ = "razana_a"

""" my_deployer.py"""

import sys
import os
import paramiko

def config(ip_adress):

    """ The config subcommand will allow installing and configuring
    Docker on the remote host.The first thing your script must be
    able to do is connect to the remote host, and make sure that
    docker-ce 19.03 is properly installed and configured.
    If the remote host happens to lack a Docker installation,
    your script will have to install it. If the Docker version
    is out-of-date, your script will have to upgrade it
    to version 19.03. """

    #checking if there is only one argument
    if len(ip_adress) == 1:
        print("Docker installation")

    else:
        raise ValueError("No arguments for config.")

    print("In config module")

def build(parameters):

    """ Your script will ensure the building of the microservices'
    images on the remote host.Your script should allow building
    all or only specific microservices using the build subcommand. """


    print("In Build module")


def deploy(parameters):

    """ The deploy subcommand accepts a list of services to deploy.
    For each of them, it must:Check whether there already is a
    container matching the microservice on the remote host
    If no container is running the microservice,create and run a container for it
    If a container is already running an outdated version of the service:
    - Stop the running container
    - Create and run a new, up-to-date container
    - If the newly-deployed container encounters any error,
    bring the old container back up
    - Otherwise, cleanup the old container
    """

    print("In deploy module")

def healthcheck(parameters):

    """ To ensure stability of your services, your Dockerfiles will implement
    Healthcheck (see the official Docker documentation).
    The healthcheck subcommand will allow peeking at the containers'
    state on the remote host.
    It must allow checking either all or only some specified containers.
    It must allow restarting the container if they are considered unhealthy.
    """ 

    print("In healthcheck module")


def interprate_cmd():

    """ Interprate commands """

    argv_unparsed = ""

    """Collecting all args"""
    for arg in sys.argv[1:]:
        argv_unparsed += arg + " "

    """Parsing args string"""
    argv_parsed = argv_unparsed.split()

    print(argv_parsed[1:])

    if argv_parsed[0] == "config":
        config(argv_parsed[1:])
    
    elif argv_parsed[0] == "build":
        build(argv_parsed[1:])
    
    elif argv_parsed[0] == "deploy":
        deploy(argv_parsed[1:])

    elif argv_parsed[0] == "healthcheck":
        healthcheck(argv_parsed[1:])
    
    else:
        raise ValueError("Unknown command: " + argv_parsed[0])

interprate_cmd()
