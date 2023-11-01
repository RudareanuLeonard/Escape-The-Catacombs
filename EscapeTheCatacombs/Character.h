#include <string>

#pragma once

class Character {
private:
	std::string m_name{};
	int m_hp{ 0 };
	int m_damageAttack{};

public:
	Character(std::string name, int hp, int damageAttack) :
		m_name{name},
		m_hp{hp},
		m_damageAttack{damageAttack}{}


};