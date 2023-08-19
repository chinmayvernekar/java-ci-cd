package com.chinmay.ci_cd;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class JavaCiCdExampleApplication {
    
    	@GetMapping
    	public String HELLO() {
    	    return "HELLO GIT LAB!!!!!!!!";
    	} 
    
    
    
    
	public static void main(String[] args) {
		SpringApplication.run(JavaCiCdExampleApplication.class, args);
	}

}
