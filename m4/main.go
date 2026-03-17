package main

import (
	"encoding/json"
	"os"
)

func main() {
	var data map[string]interface{}
	json.NewDecoder(os.Stdin).Decode(&data)

	data["answer"] = "yeeees"

	json.NewEncoder(os.Stdout).Encode(data)
}