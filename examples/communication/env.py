#!/usr/bin/env python

import os
import pyson
import pyson.runtime
import pyson.stdlib

env = pyson.runtime.Environment()

with open(os.path.join(os.path.dirname(__file__), "receiver.asl")) as source:
    env.build_agent(source, pyson.stdlib.actions)

with open(os.path.join(os.path.dirname(__file__), "receiver.asl")) as source:
    agents = env.build_agents(source, 3, pyson.stdlib.actions, name="custom_receiver")

with open(os.path.join(os.path.dirname(__file__), "sender.asl")) as source:
    agents.append(env.build_agent(source, pyson.stdlib.actions))

if __name__ == "__main__":
    env.run()
