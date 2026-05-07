//java tldr
import java.io.*;
import java.nio.file.*;
import java.text.SimpleDateFormat;
import java.util.*;

public class tldr {

    private static final String DEST_BASE = "C:\\USBBackups";
    private static final Set<String> seenDrives = new HashSet<>();

    public static void main(String[] args) {
        System.out.println("started. " + DEST_BASE);

        File baseDir = new File(DEST_BASE);
        if (!baseDir.exists()) {
            baseDir.mkdirs();
        }

        while (true) {
            try {
                checkForUsbDrives();
                Thread.sleep(5000); // check every 5 seconds
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    private static void checkForUsbDrives() {
        File[] roots = File.listRoots();
        for (File root : roots) {
            try {
                if (root.canRead() && isRemovable(root)) {
                    String path = root.getAbsolutePath();

                    if (!seenDrives.contains(path)) {
                        seenDrives.add(path);
                        backupDrive(root);
                    }
                }
            } catch (Exception e) {
                System.out.println("Error checking drive: " + e.getMessage());
            }
        }
    }

    // crude detection of removable drive (Windows-specific)
    private static boolean isRemovable(File drive) {
        long total = drive.getTotalSpace();
        // Assume drives <200GB are USB (adjust as needed)
        return total > 0 && total < (200L * 1024 * 1024 * 1024);
    }

    private static void backupDrive(File drive) {
        // Get drive letter without colon or backslash
        String driveLetter = drive
            .getAbsolutePath()
            .replace("\\", "")
            .replace(":", "");

        String ts = new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date());

        File dest = new File(DEST_BASE, driveLetter + "_" + ts);
        if (!dest.exists()) {
            dest.mkdirs();
        }

        System.out.println("[+] Backing up " + drive + " -> " + dest);
        try {
            copyDirectory(drive.toPath(), dest.toPath());
            System.out.println("[✔] Backup complete for " + drive);
        } catch (IOException e) {
            System.out.println("[!] Backup error: " + e.getMessage());
        }
    }

    private static void copyDirectory(Path source, Path target)
        throws IOException {
        Files.walk(source).forEach(path -> {
            try {
                Path dest = target.resolve(source.relativize(path).toString());
                if (Files.isDirectory(path)) {
                    if (!Files.exists(dest)) {
                        Files.createDirectories(dest);
                    }
                } else {
                    Files.copy(path, dest, StandardCopyOption.REPLACE_EXISTING);
                    System.out.println("Copied: " + dest);
                }
            } catch (IOException e) {
                System.out.println(
                    "Failed to copy " + path + ": " + e.getMessage()
                );
            }
        });
    }
}
