package selenium_test;

import java.util.Arrays;
import java.util.List;
import java.util.jar.Attributes.Name;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class seleniumtest11_ecommerce {

	public static void main(String[] args) throws InterruptedException {
		WebDriver driver = new ChromeDriver();	
		String[] itemsNeeded= {"Cucumber","Brocolli","Beetroot"};





		driver.get("https://rahulshettyacademy.com/seleniumPractise/");
		driver.manage().window().maximize();

		Thread.sleep(3000);

		addItems(driver,itemsNeeded);


		}



		public static  void addItems(WebDriver driver,String[] itemsNeeded)

		{

		int j=0;

		List<WebElement> products=driver.findElements(By.cssSelector("h4.product-name"));


		for(int i=0;i<products.size();i++)


		{


		//Brocolli - 1 Kg

		//Brocolli,    1 kg

		String[] name=products.get(i).getText().split("-");

		String formattedName=name[0].trim();


		//format it to get actual vegetable name

		//convert array into array list for easy search

		//  check whether name you extracted is present in arrayList or not-


		List itemsNeededList = Arrays.asList(itemsNeeded);



		if(itemsNeededList.contains(formattedName))

		{


		j++;

		//click on Add to cart

		driver.findElements(By.xpath("//div[@class='product-action']/button")).get(i).click();          //You should not relay on text based locater you should use any other standard locater  
                                                                                                        // also this is one fine way to parent to child

		if(j==itemsNeeded.length)

		{

		break;

		}





		}

		}

		}

	}


