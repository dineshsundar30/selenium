package selenium_test;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;

public class seleniumtest9 {
// end to end automation for a flight booking page
	public static void main(String[] args) throws InterruptedException {
        WebDriver driver = new ChromeDriver();
		driver.get("https://rahulshettyacademy.com/dropdownsPractise/");
		driver.manage().window().maximize();      

		System.out.println(driver.getTitle()); 
		// Selecting the locations
		driver.findElement(By.xpath(".//*[@id='ctl00_mainContent_ddl_originStation1_CTXT']")).click();
		driver.findElement(By.xpath("//a[@value='MAA']")).click();
		Thread.sleep(1000);
		driver.findElement(By.xpath("//div[@id='glsctl00_mainContent_ddl_destinationStation1_CTNR'] //a[@value='PNQ']")).click();
		Thread.sleep(1000);
		
		// selecting the date
		driver.findElement(By.cssSelector(".ui-state-default.ui-state-highlight.ui-state-hover")).click();
		
		// checking the return date is enabled or not
		if(driver.findElement(By.id("Div1")).getAttribute("style").contains("0.5"))

		{


		  System.out.println("its enabled");

		  Assert.assertTrue(true);

		}

		else

		{

		  Assert.assertTrue(false);

		}
		// handling the passengers count
		 driver.findElement(By.id("divpaxinfo")).click();
		  Thread.sleep(2000);
		
		
		
		   System.out.println(driver.findElement(By.id("divpaxinfo")).getText());

			for(int i=1;i<5;i++)

			{

			driver.findElement(By.id("hrefIncAdt")).click();

			}
             // handling the currency drop down in page
			driver.findElement(By.id("ctl00_mainContent_DropDownListCurrency")).click();
			driver.findElement(By.cssSelector("option[value='USD']")).click();
			
			//clicking search
			driver.findElement(By.id("ctl00_mainContent_btn_FindFlights")).click();
			}

}
