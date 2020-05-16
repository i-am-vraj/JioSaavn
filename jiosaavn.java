import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.interactions.Actions;
public class jiosaavn {
    public static void main(String[] args) {
        
        WebDriver driver = new FirefoxDriver();
        
        driver.get("http://google.com");
        
        
        driver.manage().timeouts().implicitlyWait(20L, TimeUnit.SECONDS);
        driver.manage().window().maximize();
        
        
        WebElement gmail = driver.findElement(By.xpath(".//*[@id='gbw']/div/div/div[1]/div[1]/a"));
        
        Actions action1 = new Actions(driver);
        action1.contextClick(gmail).sendKeys(Keys.ARROW_DOWN).sendKeys(Keys.ARROW_DOWN).sendKeys(Keys.ENTER).build().perform();;
    }
}