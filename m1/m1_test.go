package main

import (
	"net/http/httptest"
	"testing"
)

func TestRootEndpoint(t *testing.T) {
	req := httptest.NewRequest("GET", "/", nil)
	w := httptest.NewRecorder()

	RootHandler(w, req)

	if w.Body.String() != "Привет, мир!" {
		t.Errorf("Ожидалось 'Привет, мир!', получили '%s'", w.Body.String())
	}
}