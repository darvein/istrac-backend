demo () {
  curl -s http://localhost:8000/api/tplaces/
}

demo2 () {
  curl -X POST http://localhost:8000/api/tplaces/ \
    -H 'Content-Type: application/json' \
    -d '{"name": "New Place", "whatever": "123 Main St", "description": "40.7128"}'
}

demo
