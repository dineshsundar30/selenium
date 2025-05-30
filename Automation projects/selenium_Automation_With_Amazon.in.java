package selenium_test;
import java.util.List;
import java.util.Scanner;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class seleniumtest {

	public static void main(String[] args) throws InterruptedException {
	   WebDriver driver = new ChromeDriver();
	   driver.get("https://www.amazon.in/");
	   driver.manage().window().maximize();
	   
	   Scanner input = new Scanner(System.in);
	   System.out.println("Enter your product name: ");
	   String userinput = input.nextLine();  
	   
	  
	   driver.findElement(By.cssSelector("input[placeholder='Search Amazon.in']")).sendKeys(userinput);
	   driver.findElement(By.cssSelector("div[class='nav-search-submit nav-sprite']")).click();
	   
	   Thread.sleep(5000);
	   
	   	driver.findElement(By.cssSelector("i[class*=' a-star-medium-4']")).click();
	   	Thread.sleep(5000);
	   	driver.findElement(By.xpath("//*[text()='50% Off or more']")).click();
		Thread.sleep(1000);
		for (int i = 1; i <= 5; i++) {
			Thread.sleep(1000);
		    String cssSelector = String.format("div[data-cel-widget='search_result_%s']", i);
		    System.out.println(driver.findElement(By.cssSelector(cssSelector)).getText());
		    System.out.println("------------------------------------------------------------------------------------------------");
		    Thread.sleep(1000);
		}
	}

}
