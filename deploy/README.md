# Orbit Graph Deploy Code

```bash
ansible-playbook -i hosts.yml all.yml --extra-vars "ansible_user=ubuntu"
```

`all.yml` playbook initializes deployment machine, while `redeploy.yml` just
redeploys Docker containers if required.

## Kafka

* [How to properly configure Kafka?](https://www.confluent.io/blog/kafka-client-cannot-connect-to-broker-on-aws-on-docker-etc)

## Still Manual

* If Memgraph deps change, Memgraph docker images has to be manually rebuilt
  (Ansible will just pick the image on the right path).

* Frontend has to be manually built locally and then the `dist` folder is just
  uploaded and mounted on the server.
