package com.article.finder.service;

import com.google.auth.oauth2.GoogleCredentials;
import com.google.firebase.FirebaseApp;
import com.google.firebase.FirebaseOptions;
import org.springframework.stereotype.Service;
import org.springframework.util.ResourceUtils;

import javax.annotation.PostConstruct;
import java.io.File;
import java.io.FileInputStream;

@Service
public class FBinitialize {

    @PostConstruct
    public void initialize() {
        try{

            File file = ResourceUtils.getFile("classpath:article-finder-bb398-firebase-adminsdk-6fxyp-28a9af4743.json");

            FileInputStream serviceAccount =
                    new FileInputStream(file);

            FirebaseOptions options = new FirebaseOptions.Builder()
                    .setCredentials(GoogleCredentials.fromStream(serviceAccount))
                    .setDatabaseUrl("https://db-spring-afus-default-rtdb.firebaseio.com")
                    .build();

            FirebaseApp.initializeApp(options);

        }catch(Exception e){
            e.printStackTrace();
        }
    }

}


