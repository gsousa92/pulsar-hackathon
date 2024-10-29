# pulsar-hackathon
Apache pulsar mvp


# Build

- Initialize the project
  ```bash
  $ ./init.sh
  ```
- Run the pulsar service
  ```bash
  $ docker-compose up -d
  ```

## Pulsar Manager

You can access the Pulsar Manager UI by visiting http://localhost:9527/. Create a superuser following the instructions
[here](https://pulsar.apache.org/docs/next/administration-pulsar-manager/#3-set-the-administrator-account-and-password).
Then login and create a new environment with the following:
- Service URL: `http://pulsar-broker:8080`
- Bookie URL: `http://pulsar-bookie:3181`
