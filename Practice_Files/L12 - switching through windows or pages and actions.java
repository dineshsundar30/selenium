package selenium_test;



import java.time.Duration;
import java.util.Iterator;
import java.util.Set;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

public class seleniumtest13 {
// switching through windows or pages and actions
	public static void main(String[] args) throws InterruptedException {
		WebDriver driver = new ChromeDriver();
		driver.get("https://www.amazon.in/");
		Actions a = new Actions(driver);
		driver.manage().window().maximize();
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(50));
		
		//a.moveToElement(driver.findElement(By.id("itaftk-9viajt-56y3a2-4dnvr6"))).build().perform();
		
		WebElement move = driver.findElement(By.cssSelector("a[data-csa-c-slot-id='nav_cs_0']"));
		a.moveToElement(move).click().build().perform();
		driver.navigate().back();
		a.moveToElement(driver.findElement(By.cssSelector("input[placeholder='Search Amazon.in']"))).click().keyDown(Keys.SHIFT).sendKeys("iphone").doubleClick().build().perform();
		
		//    a.moveToElement(move).contextClick().build().perform();  // to right lick in the element
		
		
		
		driver.navigate().to("https://rahulshettyacademy.com/loginpagePractise/#");

		driver.findElement(By.cssSelector(".blinkingText")).click();

		Set<String> windows = driver.getWindowHandles(); // it will get the all windows opened by selenium driver [parentid,childid,subchildId]

		Iterator<String>it = windows.iterator();

		String parentId = it.next();

		String childId = it.next();

		driver.switchTo().window(childId);

		System.out.println(driver.findElement(By.cssSelector(".im-para.red")).getText());

		driver.findElement(By.cssSelector(".im-para.red")).getText();

		String emailId= driver.findElement(By.cssSelector(".im-para.red")).getText().split("at")[1].trim().split(" ")[0];

		driver.switchTo().window(parentId);

		driver.findElement(By.id("username")).sendKeys(emailId);
		driver.quit();

	}

}
