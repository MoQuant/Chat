#include <iostream>
#include <string>
#include <sstream>
#include <cpprest/ws_client.h>

using namespace web;
using namespace web::websockets::client;

int main()
{
    std::string message;
    std::string url = "ws://localhost:8080";
    
    websocket_client client;
    client.connect(url).wait();

    websocket_outgoing_message out_msg;
    while(true){
        std::cout << "Enter your sentence: ";
        std::getline(std::cin, message);
        out_msg.set_utf8_message(message);
        client.send(out_msg);
        std::cout << std::endl;
        std::cout << std::endl;
    }

    client.close().wait();

    return 0;
}