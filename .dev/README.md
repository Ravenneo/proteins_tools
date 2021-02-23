# Docker for Development

### Build docker for Development

```bash
docker build -f .dev/Dockerfile -t protein_tool:dev .
```
### Run docker for Development

```bash
docker run -it --rm -v $(pwd):/home/bio/project protein_tool:dev
```

`$(pwd)` is inside of the repository
