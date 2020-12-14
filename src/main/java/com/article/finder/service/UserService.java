package com.article.finder.service;

import com.article.finder.models.Users;
import com.google.api.core.ApiFuture;
import com.google.cloud.firestore.DocumentReference;
import com.google.cloud.firestore.DocumentSnapshot;
import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.WriteResult;
import com.google.firebase.cloud.FirestoreClient;
import org.springframework.stereotype.Service;

import java.util.concurrent.ExecutionException;

@Service
public class UserService {

    private Firestore dbFirestore;

    UserService(Firestore dbFirestore){
        this.dbFirestore = dbFirestore;
    }

    public static final String COL_NAME = "users";

    public Users getUser(String uid) throws InterruptedException, ExecutionException {
        DocumentReference documentReference = dbFirestore.collection(COL_NAME).document(uid);
        ApiFuture<DocumentSnapshot> future = documentReference.get();
        DocumentSnapshot document = future.get();

        if(document.exists()) {
            Users user = document.toObject(Users.class);
            return user;
        }else {
            return null;
        }
    }

    public void extractionOfFile(String uid, String filename) throws InterruptedException, ExecutionException{

    }

}
