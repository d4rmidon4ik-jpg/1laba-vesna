package main

import (
	"bytes"
	"encoding/json"
	"testing"
)

func TestGoLogic(t *testing.T) {
	input := map[string]interface{}{"message": "1 laba?"}
	inputJSON, _ := json.Marshal(input)
	
	stdin := bytes.NewReader(inputJSON)
	stdout := &bytes.Buffer{}
	
	var data map[string]interface{}
	json.NewDecoder(stdin).Decode(&data)
	data["answer"] = "yeeees"
	json.NewEncoder(stdout).Encode(data)
	
	var output map[string]interface{}
	json.NewDecoder(stdout).Decode(&output)
	
	if output["answer"] != "yeeees" {
		t.Errorf("Ожидалось 'yeeees', получили '%v'", output["answer"])
	}
}