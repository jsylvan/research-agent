
## Docker & Deployment

- Build image:
  \`\`\`bash
  docker build -t my-multimodel-agent .
  \`\`\`
- Run container:
  \`\`\`bash
  docker run -it --rm -p 8000:8000 my-multimodel-agent
  \`\`\`
- Or use docker-compose:
  \`\`\`bash
  docker-compose up --build
  \`\`\`

## Logging & Monitoring

- Use \`logging_utils.configure_logging\` at the start of main, or in each role as desired.
- Connect to Datadog/Prometheus for advanced monitoring as needed.
