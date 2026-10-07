package com.netmap.ai.model;

public class GenerateRequest {
    private int count;

    public GenerateRequest() {
    }

    public GenerateRequest(int count) {
        this.count = count;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }
}
