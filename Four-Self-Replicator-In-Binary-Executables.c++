#include <iostream>
#include <fstream>
#include <random>
#include <string>

std::string generateRandomString(int length) {
    const std::string alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, alphabets.length() - 1);

    std::string randomString;
    for (int i = 0; i < length; ++i) {
        randomString += alphabets[dis(gen)];
    }
    return randomString + ".exe";
}

int main(int argc, char* argv[]) {
    if (argc < 1) {
        std::cerr << "Usage: " << argv[0] << " <filename>\n";
        return 1;
    }

    std::string selfScript(argv[0]);
    std::ifstream inputFile(selfScript, std::ios::binary);
    if (!inputFile) {
        std::cerr << "Error: Unable to open file: " << selfScript << std::endl;
        return 1;
    }

    std::string data((std::istreambuf_iterator<char>(inputFile)), (std::istreambuf_iterator<char>()));

    std::string fileName = generateRandomString(std::rand() % 5 + 4); // Random filename length between 4 and 8
    std::ofstream outputFile(fileName, std::ios::binary);
    if (!outputFile) {
        std::cerr << "Error: Unable to create file: " << fileName << std::endl;
        return 1;
    }

    outputFile.write(data.c_str(), data.size());

    std::cout << "File replicated as: " << fileName << std::endl;

    return 0;
}
