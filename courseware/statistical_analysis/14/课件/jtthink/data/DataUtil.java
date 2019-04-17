package com.jtthink.data;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import okhttp3.*;

import java.io.IOException;
import java.util.HashMap;

public class DataUtil {
   public static  String add(HashMap hashMap) throws IOException {

       ObjectMapper objectMapper=new ObjectMapper();
       MediaType JSON_TYPE=MediaType.parse("application/json; charset=utf-8");
       RequestBody requestBody=RequestBody.create(JSON_TYPE,objectMapper.writeValueAsString(hashMap));

       Request request=new Request.Builder()
               .url("http://localhost:5000/input/employess")
               .post(requestBody)
               .build();
       OkHttpClient okHttpClient=new OkHttpClient();
      Response response=okHttpClient.newCall(request).execute();
      if(response.isSuccessful()){
        return response.body().string();
      }
      return "";

   }
}
