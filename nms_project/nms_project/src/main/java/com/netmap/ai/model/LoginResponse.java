package com.netmap.ai.model;

public class LoginResponse {
    private boolean authenticated;
    private String username;
    private String message;

    public LoginResponse() {
    }

    public LoginResponse(boolean authenticated, String username, String message) {
        this.authenticated = authenticated;
        this.username = username;
        this.message = message;
    }

    public boolean isAuthenticated() {
        return authenticated;
    }

    public void setAuthenticated(boolean authenticated) {
        this.authenticated = authenticated;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
