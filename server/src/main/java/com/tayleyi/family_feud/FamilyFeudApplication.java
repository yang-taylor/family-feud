package com.tayleyi.family_feud;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class FamilyFeudApplication {

	public static void main(String[] args) {
		SpringApplication.run(FamilyFeudApplication.class, args);
	}

	@GetMapping("/random")
	public String hello(@RequestParam(value = "n", defaultValue = "20") String n) {
		int numberOfQuestions = Integer.parseInt(n);
		return String.format("Hello %s!", n);
	}
}