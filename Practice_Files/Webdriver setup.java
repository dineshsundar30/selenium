package selenium_test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class intro {

	public static void main(String[] args) {
	
		//System.setProperty("WebDriver.Chrome.driver", "path..")
        WebDriver driver = new ChromeDriver();
        driver.get("https://financialgear.blogspot.com/");
        System.out.println(driver.getTitle());
        System.out.println(driver.getCurrentUrl());
        driver.close(); // its close current or opened by selenium
        driver.quit(); //its close all associated windows
	
	
        /* To run on browser
        System.setProperty("WebDriver.gecko.driver", "path..")
        WebDriver driver = new FirefoxDriver();
        driver.get("https://financialgear.blogspot.com/");
        System.out.println(driver.getTitle());   
        
        To run on Edge browser
        System.setProperty("WebDriver.edge.driver", "path..")
        WebDriver driver = new EdgeDriver();
        driver.get("https://financialgear.blogspot.com/");
        System.out.println(driver.getTitle());    */
     
	
	
	
	}

}
