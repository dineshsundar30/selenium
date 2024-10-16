package selenium_test;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;

// counting the checkboxs and Asserts
public class seleniumtest6 {

	public static void main(String[] args) throws InterruptedException   {
        WebDriver driver = new ChromeDriver();	
		driver.get("https://rahulshettyacademy.com/dropdownsPractise/");	
		driver.manage().window().maximize();
		Assert.assertFalse(driver.findElement(By.cssSelector("input[id*='SeniorCitizenDiscount']")).isSelected());

		//Assert.assertFalse(true);System.out.println(driver.findElement(By.cssSelector("input[id*='SeniorCitizenDiscount']")).isSelected());

		 driver.findElement(By.cssSelector("input[id*='SeniorCitizenDiscount']")).click();

		 System.out.println(driver.findElement(By.cssSelector("input[id*='SeniorCitizenDiscount']")).isSelected());

		 Assert.assertTrue(driver.findElement(By.cssSelector("input[id*='SeniorCitizenDiscount']")).isSelected());

          // to find num of checkbox in page
		 
		  System.out.println(driver.findElements(By.cssSelector("input[type='checkbox']")).size());
		  driver.findElement(By.id("divpaxinfo")).click();
		  Thread.sleep(2000);
		
		
		
		   System.out.println(driver.findElement(By.id("divpaxinfo")).getText());

			for(int i=1;i<5;i++)

			{

			driver.findElement(By.id("hrefIncAdt")).click();

			}

			driver.findElement(By.id("btnclosepaxoption")).click();
            Assert.assertEquals(driver.findElement(By.id("divpaxinfo")).getText(), "5 Adult");
            System.out.println(driver.findElement(By.id("divpaxinfo")).getText());
            
            
       
            // Here we are checking the the element's is enabled or not 
    		
    		// some time this isEnabled will not work before and after clicking the button both will show true below 
    		
    		System.out.println(driver.findElement(By.id("ctl00_mainContent_rbtnl_Trip_1")).isEnabled());  
    		
    		
            // then we need to find while enable which element's is changing in page find and add it in condition like below
    		
    		System.out.println(driver.findElement(By.id("Div1")).getAttribute("style"));

    		driver.findElement(By.id("ctl00_mainContent_rbtnl_Trip_1")).click();
    		System.out.println(driver.findElement(By.id("ctl00_mainContent_rbtnl_Trip_1")).isEnabled());

    		System.out.println(driver.findElement(By.id("Div1")).getAttribute("style"));

    		if(driver.findElement(By.id("Div1")).getAttribute("style").contains("1"))

    		{


    		System.out.println("its enabled");

    		Assert.assertTrue(true);

    		}

    		else

    		{

    		Assert.assertTrue(false);

    		}

		}

	}


