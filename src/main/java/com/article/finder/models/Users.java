package com.article.finder.models;

public class Users {
    private String emailIdUser;
    private String imageUrl;
    private String uid;

    public Users(){

    }

    public Users(String emailIdUser, String imageUrl, String uid) {
        this.emailIdUser = emailIdUser;
        this.imageUrl = imageUrl;
        this.uid = uid;
    }

    public String getEmailIdUser() {
        return emailIdUser;
    }

    public void setEmailIdUser(String emailIdUser) {
        this.emailIdUser = emailIdUser;
    }

    public String getImageUrl() {
        return imageUrl;
    }

    public void setImageUrl(String imageUrl) {
        this.imageUrl = imageUrl;
    }

    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
}
