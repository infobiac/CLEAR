pragma solidity ^0.4.7;
import "remix_tests.sol"; // this import is automatically injected by Remix.

contract Clarity {
    address user;
    string public metadata;

    mapping(address=>string) public verifiers;
    address[] pending;
    address[] approved;

    function Clarity(string metadata, address user, string apiURL) public {
        user = user;
        metadata = metadata;
        verifiers[msg.sender] = apiURL;
    }

    function request_access() public{
        pending.push(msg.sender);
    }

    function grant_access(address seeker) public {
        if (user == msg.sender) {
            uint idx = 0;
            bool present = false;
            for (uint i = 0; i < pending.length; i++){
                if (pending[i] == seeker) {
                    idx = i;
                    present = true;
                }
            }
            if (present) {
                approved.push(pending[idx]);
                for (uint y = idx; y < pending.length - 1; y++){
                    pending[y] = pending[y+1];
                }
                delete pending[pending.length-1];
                pending.length--;
            }
        }
    }

    function getpending() constant public returns(address[]){
        if (user == msg.sender) {
            return pending;
        }
    }

    function check_access(address seeker) constant public returns(bool){
        bool present = false;
        for (uint i = 0; i < pending.length; i++){
            if (pending[i] == seeker) {
                present = true;
            }
        }
        return present;
    }

}
