package selenium_test;
import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
public class seleniumtest {
//Finding locators and the different ways
	public static void main(String[] args) throws InterruptedException {

		//implicit wait - 2 seconds time out it's will wait for element's to be showed up for entered time
		//System.setProperty("webdriver.chrome.driver", "/Users/rahulshetty/Documents/chromedriver");
		WebDriver driver = new ChromeDriver();
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(5));  //it will wait to attribute to be showed up
		
		driver.get("https://rahulshettyacademy.com/locatorspractice/");

		driver.findElement(By.id("inputUsername")).sendKeys("Dk");

		driver.findElement(By.name("inputPassword")).sendKeys("hello123");

		driver.findElement(By.className("signInBtn")).click(); // if you seen space between the class name it's a 2 class name

		System.out.println(driver.findElement(By.cssSelector("p.error")).getText());

		driver.findElement(By.linkText("Forgot your password?")).click();

		Thread.sleep(1000);   // it will wait to get a stable  

		driver.findElement(By.xpath("//input[@placeholder='Name']")).sendKeys("John");

		driver.findElement(By.cssSelector("input[placeholder='Email']")).sendKeys("john@rsa.com");

		driver.findElement(By.xpath("//input[@type='text'][2]")).clear();      // finding element by indexing with xpath if we don't have unique element's

		driver.findElement(By.cssSelector("input[type='text']:nth-child(3)")).sendKeys("john@gmail.com");  // finding element by indexing with css if we don't have unique element's 

		driver.findElement(By.xpath("//form/input[3]")).sendKeys("9864353253");  // here we can get the selector based on the parent to child tags using parent tag and child tag like //parenttag/childtag

		driver.findElement(By.cssSelector(".reset-pwd-btn")).click();

		System.out.println(driver.findElement(By.cssSelector("form p")).getText());   // here we can get the selector based on the parent to child tags using parent tag and child tag like parenttag space childtag

		driver.findElement(By.xpath("//div[@class='forgot-pwd-btn-conainer']/button[1]")).click();  // example for combination of 3 selectors like path,indexing,parent to child

		Thread.sleep(1000);

		driver.findElement(By.cssSelector("#inputUsername")).sendKeys("Dinesh");

		driver.findElement(By.cssSelector("input[type*='pass']")).sendKeys("rahulshettyacademy");  // if we use a * it will scan all the partial value like that

		driver.findElement(By.id("chkboxOne")).click();

		driver.findElement(By.xpath("//button[contains(@class,'submit')]")).click();  // to scan with the partial value in xpath
		
		
		}

}
