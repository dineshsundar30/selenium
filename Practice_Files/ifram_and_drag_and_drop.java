package selenium_test;



import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

public class testifram {

	public static void main(String[] args) {
		WebDriver driver = new ChromeDriver();
		driver.get("https://the-internet.herokuapp.com/");
		driver.manage().window().maximize();
		driver.findElement(By.linkText("Nested Frames")).click();
        driver.switchTo().frame("frame-top");
		driver.switchTo().frame("frame-middle");
		System.out.println(driver.findElement(By.id("content")).getText());

	     driver.navigate().to("https://jqueryui.com/droppable/");
	     System.out.println(driver.findElements(By.tagName("iframe")).size());

	     driver.switchTo().frame(driver.findElement(By.className("demo-frame")));

	     driver.findElement(By.id("draggable")).click();

	     Actions a = new Actions(driver);

	     WebElement drag = driver.findElement(By.id("draggable"));

	     WebElement drop = driver.findElement(By.id("droppable"));

	     a.dragAndDrop(drag, drop).build().perform();

	     driver.switchTo().defaultContent();

	        driver.quit();
		
		
	}

}
