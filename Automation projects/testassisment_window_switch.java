package selenium_test;

import java.util.Iterator;
import java.util.Set;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class testassisment_window_switch {

	public static void main(String[] args) {
		WebDriver driver = new ChromeDriver();
		driver.get("https://the-internet.herokuapp.com/");
		driver.findElement(By.xpath("//a[text()='Multiple Windows']")).click();
		driver.findElement(By.cssSelector("a[href*='windows']")).click();
		Set<String> windows = driver.getWindowHandles();
		Iterator<String> it = windows.iterator();
		String parentId = it.next();
		//String childId = it.next();
		driver.switchTo().window(it.next());
		System.out.println(driver.findElement(By.cssSelector(".example")).getText());
		driver.switchTo().window(parentId);
	    System.out.println(driver.findElement(By.cssSelector("div[id='content']  div h3")).getText());
		//System.out.println(driver.findElement(By.xpath("//div[@id='content']/div/h3")).getText());
		driver.quit();
		
	} 

}
