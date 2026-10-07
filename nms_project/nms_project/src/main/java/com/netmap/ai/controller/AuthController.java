package com.netmap.ai.controller;

import com.netmap.ai.model.LoginRequest;
import com.netmap.ai.model.LoginResponse;
import jakarta.servlet.http.HttpSession;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class AuthController {

    private static final String DEMO_USER = "admin";
    private static final String DEMO_PASS = "admin123";
    private static final String SESSION_USER_KEY = "LOGGED_IN_USER";

    @PostMapping("/login")
    public ResponseEntity<LoginResponse> login(@RequestBody LoginRequest request, HttpSession session) {
        if (request != null &&
                DEMO_USER.equals(request.getUsername()) &&
                DEMO_PASS.equals(request.getPassword())) {
            session.setAttribute(SESSION_USER_KEY, DEMO_USER);
            return ResponseEntity.ok(new LoginResponse(true, DEMO_USER, "Login successful. Welcome to NetMap AI!"));
        } else {
            return ResponseEntity.status(401)
                    .body(new LoginResponse(false, null, "Invalid username or password. Demo credentials: admin / admin123"));
        }
    }

    @PostMapping("/logout")
    public ResponseEntity<LoginResponse> logout(HttpSession session) {
        session.removeAttribute(SESSION_USER_KEY);
        session.invalidate();
        return ResponseEntity.ok(new LoginResponse(false, null, "Successfully logged out."));
    }

    @GetMapping("/auth/status")
    public ResponseEntity<LoginResponse> checkStatus(HttpSession session) {
        Object user = session.getAttribute(SESSION_USER_KEY);
        if (user != null) {
            return ResponseEntity.ok(new LoginResponse(true, user.toString(), "Authenticated"));
        } else {
            return ResponseEntity.ok(new LoginResponse(false, null, "Not authenticated"));
        }
    }
}
