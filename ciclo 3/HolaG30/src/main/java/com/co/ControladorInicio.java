
package com.co;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class ControladorInicio {
    
    @GetMapping("/")
    public String inicio(){
        return "index";
}
        
}