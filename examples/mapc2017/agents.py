#!/usr/bin/env python

import asyncio
import pyson.runtime
import logging
from mapc2017 import (actions, Agent, Environment)


pyson.get_logger("pyson.mapc2017").setLevel(logging.DEBUG)


async def main():
    env = Environment()

    with open("agent1.asl") as source:
        agent1 = env.build_agent(source, actions, Agent, "agentA1")
    with open("agent1.asl") as source:
        agent2 = env.build_agent(source, actions, Agent, "agentA2")
    with open("agent1.asl") as source:
        agent3 = env.build_agent(source, actions, Agent, "agentA3")
    with open("agent1.asl") as source:
        agent4 = env.build_agent(source, actions, Agent, "agentA4")
    with open("agent1.asl") as source:
        agent5 = env.build_agent(source, actions, Agent, "agentA5")
    with open("agent1.asl") as source:
        agent6 = env.build_agent(source, actions, Agent, "agentA6")

    await agent1.connect("agentA1", "1")
    #await agent2.connect("agentA2", "1")
    #await agent3.connect("agentA3", "1")
    #await agent4.connect("agentA4", "1")
    #await agent5.connect("agentA5", "1")
    #await agent6.connect("agentA6", "1")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        loop.run_forever()
    finally:
        loop.close()
