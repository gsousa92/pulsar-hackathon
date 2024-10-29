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

You can access the Pulsar Manager UI by visiting http://localhost:9527/. Create a new environment with the following:
- Service URL: `http://pulsar-broker:8080`
- Bookie URL: `http://pulsar-bookie:3181`
