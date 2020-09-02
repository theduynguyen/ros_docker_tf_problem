# Reproduce /tf subscription error and solution after Image update on 20.08.2020

To setup the problem, start script

```bash
./setup_problem.sh
```

The containers tf_problem and tf_solution contain the exact same ROS Nodes. However, only the solution container is able to receive the latest tf messages.
