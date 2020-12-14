package com.article.finder.controller;

import com.article.finder.models.Users;
import com.article.finder.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.concurrent.ExecutionException;

@RestController
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("/user/get")
    public Users getUserAPI(@RequestParam String uid) throws InterruptedException, ExecutionException{
        return userService.getUser(uid);
    }

//    @GetMapping("/user/uploadFile")
//    public String extractTextOfUploadedFile(@RequestParam String uid, @RequestParam String filename) throws InterruptedException, ExecutionException{
//
//    }

}
