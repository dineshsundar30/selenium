package selenium_test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
public class seleniumtest3 {

	public static void main(String[] args) {
	
		WebDriver driver = new ChromeDriver();

		// Sibling - Child to parent traverse

		//header/div/button[1]/following-sibling::button[1]

		driver.get("https://rahulshettyacademy.com/AutomationPractice/");

		System.out.println(driver.findElement(By.xpath("//header/div/button[1]/following-sibling::button[1]")).getText());  //moving parent to child

		System.out.println(driver.findElement(By.xpath("//header/div/button[1]/parent::div/button[2]")).getText()); // moving child to parent
		
		System.out.println("---------------------------------------------------------------------");
		
	
		
		driver.manage().window().maximize();

		driver.get("http://google.com");

		driver.navigate().to("https://rahulshettyacademy.com");

		driver.navigate().back();

		driver.navigate().forward();
		
		driver.close();

	}

}
