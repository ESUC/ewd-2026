window.addEventListener('DOMContentLoaded', () => {

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            const id = entry.target.getAttribute('id');
            const link = document.querySelector(`ol li a[href="#${id}"]`);
            if (!link) return;
            if (entry.intersectionRatio > 0) {
                link.parentElement.classList.add('active');
            } else {
                link.parentElement.classList.remove('active');
            }
        });
    });

    document.querySelectorAll('section[id]').forEach((section) => {
        observer.observe(section);
    });

    initExpo();
});

function search() {
    let input = document.getElementById("search").value.replace(/[^0-9a-z]/gi, '').toLowerCase();
    let cards = document.getElementsByClassName("card");
    for (let item of cards) {
        if (item.dataset.names.toLowerCase().search(input) == -1) {
            document.getElementById(item.id).style.display = 'none';
        } else {
            document.getElementById(item.id).style.display = 'grid';
        }
    }
}

function initExpo() {
    const root = document.getElementById("expo");
    if (!root) return;

    const orgs = JSON.parse(document.getElementById("expo-orgs-data").textContent);
    const departments = JSON.parse(document.getElementById("expo-dept-data").textContent);
    const orgById = Object.fromEntries(orgs.map((org) => [org.id, org]));
    const orgByTable = {};
    orgs.forEach((org) => {
        (org.tables || []).forEach((table) => {
            orgByTable[table] = org;
        });
    });

    const deptColor = Object.fromEntries(departments.map((dept) => [dept.id, dept.color]));
    const mapMount = document.getElementById("expo-map");
    const liveEl = document.getElementById("expo-live");
    const emptyEl = document.getElementById("expo-empty");
    const searchInput = document.getElementById("expo-search");
    const chips = Array.from(root.querySelectorAll(".expo-chip"));
    const cards = Array.from(root.querySelectorAll(".expo-card"));
    const deptGroups = Array.from(root.querySelectorAll("[data-dept-group]"));

    let activeDept = "all";
    let activeOrgId = null;
    let query = "";

    drawMap(mapMount, orgs, deptColor);
    const tableNodes = Array.from(mapMount.querySelectorAll(".expo-table"));

    function matchesQuery(org, card) {
        if (!query) return true;
        const haystack = [
            org.full_name,
            org.short_name,
            org.department_name,
            org.table,
            String(org.tables && org.tables.join(" ")),
            card && card.dataset.names
        ].join(" ").toLowerCase();
        return haystack.includes(query);
    }

    function applyFilters() {
        let visible = 0;
        cards.forEach((card) => {
            const org = orgById[card.dataset.org];
            const deptOk = activeDept === "all" || card.dataset.dept === activeDept;
            const show = deptOk && matchesQuery(org, card);
            card.hidden = !show;
            if (show) visible += 1;
        });
        deptGroups.forEach((group) => {
            const anyVisible = group.querySelector(".expo-card:not([hidden])");
            group.hidden = !anyVisible;
        });
        emptyEl.hidden = visible > 0;

        tableNodes.forEach((node) => {
            const org = orgByTable[node.dataset.table];
            const deptOk = activeDept === "all" || (org && org.department === activeDept);
            const queryOk = !org || matchesQuery(org);
            node.classList.toggle("is-dim", !(deptOk && queryOk));
            node.classList.toggle("is-active", !!(org && org.id === activeOrgId));
        });
        cards.forEach((card) => {
            card.classList.toggle("is-active", card.dataset.org === activeOrgId && !card.hidden);
        });
    }

    function selectOrg(orgId, fromCard) {
        const org = orgById[orgId];
        if (!org) return;
        activeOrgId = orgId;
        liveEl.textContent = `${org.full_name}, table ${org.table}, ${org.department_name}`;
        applyFilters();

        const card = root.querySelector(`.expo-card[data-org="${orgId}"]`);
        if (card && !fromCard) {
            card.scrollIntoView({ block: "nearest", behavior: "smooth" });
        }
    }

    chips.forEach((chip) => {
        chip.addEventListener("click", () => {
            activeDept = chip.dataset.dept;
            chips.forEach((other) => {
                const on = other === chip;
                other.classList.toggle("is-active", on);
                other.setAttribute("aria-pressed", on ? "true" : "false");
            });
            applyFilters();
        });
    });

    searchInput.addEventListener("input", () => {
        query = searchInput.value.trim().toLowerCase();
        applyFilters();
    });

    tableNodes.forEach((node) => {
        const activate = (event) => {
            event.preventDefault();
            const org = orgByTable[node.dataset.table];
            if (org) selectOrg(org.id, false);
        };
        node.addEventListener("click", activate);
        node.addEventListener("keydown", (event) => {
            if (event.key === "Enter" || event.key === " ") activate(event);
        });
    });

    cards.forEach((card) => {
        const highlight = () => selectOrg(card.dataset.org, true);
        card.addEventListener("mouseenter", highlight);
        card.addEventListener("focus", highlight);
    });

    applyFilters();

    const hash = window.location.hash.replace("#", "");
    if (hash.startsWith("table-")) {
        const org = orgByTable[Number(hash.slice(6))];
        if (org) selectOrg(org.id, false);
    } else if (hash.startsWith("org-") && orgById[hash.slice(4)]) {
        selectOrg(hash.slice(4), true);
    }
}

function drawMap(mount, orgs, deptColor) {
    const orgByTable = {};
    orgs.forEach((org) => {
        (org.tables || []).forEach((table) => {
            orgByTable[table] = org;
        });
    });

    // Percent positions, centered on each numbered table in the floor-plan JPG.
    const positions = {
        22: [73.35, 5.35],
        21: [73.35, 10.55],
        17: [32.45, 15.55],
        18: [36.65, 15.55],
        19: [40.85, 15.55],
        20: [45.05, 15.55],
        23: [42.95, 23.65],
        24: [42.95, 26.65],
        25: [42.95, 29.65],
        26: [42.95, 32.75],
        27: [42.95, 35.85],
        28: [42.95, 38.95],
        29: [42.95, 42.05],
        6: [53.85, 24.85],
        7: [57.85, 24.85],
        8: [61.85, 24.85],
        9: [65.85, 24.85],
        10: [69.85, 24.85],
        11: [73.85, 24.85],
        5: [55.05, 28.55],
        4: [55.05, 31.85],
        3: [55.05, 35.15],
        2: [55.05, 38.45],
        1: [55.05, 41.55],
        12: [61.15, 28.75],
        13: [61.15, 32.45],
        14: [61.15, 36.15],
        15: [68.55, 42.85],
        16: [73.35, 42.85],
        43: [31.35, 77.05],
        44: [31.35, 81.05],
        45: [42.05, 77.05],
        46: [42.05, 81.05],
        38: [48.75, 74.85],
        39: [48.75, 78.15],
        40: [48.75, 81.45],
        41: [59.85, 77.15],
        42: [59.85, 81.15],
        36: [71.15, 77.05],
        37: [71.15, 81.05],
        33: [34.5, 89.25],
        34: [39.2, 89.25],
        35: [43.95, 89.25],
        30: [59.65, 89.25],
        31: [64.15, 89.25],
        32: [68.65, 89.25]
    };

    Object.keys(positions).forEach((n) => {
        const num = Number(n);
        const [x, y] = positions[n];
        const org = orgByTable[num];
        const color = org ? (deptColor[org.department] || "#648bba") : "#888";
        const label = org ? `Table ${n}: ${org.full_name}` : `Table ${n}`;
        const button = document.createElement("button");
        button.type = "button";
        button.className = "expo-table";
        button.dataset.table = n;
        button.dataset.org = org ? org.id : "";
        button.dataset.dept = org ? org.department : "";
        button.setAttribute("aria-label", label);
        button.textContent = n;
        button.style.left = `${x}%`;
        button.style.top = `${y}%`;
        button.style.setProperty("--dot-color", color);
        mount.appendChild(button);
    });
}
