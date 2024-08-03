#!/bin/bash

# wait-for-it.sh script to complete database creation

set -e

host="$1"
shift
cmd="$@"    

until nc -z "$host" 5432; do
  echo "Waiting for database to be ready..."
  sleep 1
done

echo "Database is ready. Executing command."
exec $cmd
