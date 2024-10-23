package selenium_test;
import java.time.Duration;
import java.util.Arrays;
import java.util.List;


import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.Wait;
import org.openqa.selenium.support.ui.WebDriverWait;

import com.google.common.base.Function;
public class seleniumtest12 {

	public static void main(String[] args) throws InterruptedException {
		//Wait handling implicitlyWait, explicit wait

       

		WebDriver driver=new ChromeDriver();

	    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(50));  //implicitlyWait

		WebDriverWait w = new WebDriverWait(driver , Duration.ofSeconds(5));  //explicit wait initialization we have two wait's in explicit 
		                                                                           //one is WebDriverwait second is Fluent wait 

		String[] itemsNeeded= {"Cucumber","Brocolli","Beetroot"};

		driver.get("https://rahulshettyacademy.com/seleniumPractise/");

		Thread.sleep(3000);

		addItems(driver,itemsNeeded);

		driver.findElement(By.cssSelector("img[alt='Cart']")).click();

		driver.findElement(By.xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]")).click();

		w.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector("input.promoCode")));



		driver.findElement(By.cssSelector("input.promoCode")).sendKeys("rahulshettyacademy");

		driver.findElement(By.cssSelector("button.promoBtn")).click();

		

		w.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector("span.promoInfo")));  //explicit wait deceleration
        
		            //---------------The below code is just for our reference-------------------
        
		//Fluent wait implementation                                                                       
		
        Wait<WebDriver> wait = new FluentWait<>(driver).withTimeout(Duration.ofSeconds(30)).pollingEvery(Duration.ofSeconds(3)).ignoring(NoSuchElementException.class);
        WebElement foo = wait.until(new Function<WebDriver, WebElement>() {            
        public WebElement apply(WebDriver driver) {                
        try {                    
        WebElement element = driver.findElement(By.cssSelector("span.promoInfo"));                    
        if (element.isDisplayed()) {                        
            return element;                    
                                   }                
          } catch (NoSuchElementException ignored) {                
                                                  }                
        return null;            
                                             }        
                                    });
        if (foo != null) {            
        System.out.println("From Fluent wait: "+foo.getText());        
        } else {            
        System.out.println("Element not displayed or not found within the specified timeout.");        
        }


		System.out.println("From Explicit wait: "+ driver.findElement(By.cssSelector("span.promoInfo")).getText());


		}



		public static  void addItems(WebDriver driver,String[] itemsNeeded)

		{

		int j=0;

		List<WebElement> products=driver.findElements(By.cssSelector("h4.product-name"));


		for(int i=0;i<products.size();i++)


		{

		String[] name=products.get(i).getText().split("-");

		String formattedName=name[0].trim();


		List<String> itemsNeededList = Arrays.asList(itemsNeeded);



		if(itemsNeededList.contains(formattedName))

		{


		j++;

		//click on Add to cart

		driver.findElements(By.xpath("//div[@class='product-action']/button")).get(i).click();


		if(j==itemsNeeded.length)

		{
			
		break;

		}


		}

		}
 

	}

}


